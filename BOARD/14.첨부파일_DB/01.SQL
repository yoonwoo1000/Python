-- board 테이블의 bIDX를 참조하는 attach 테이블
/*
create table 테이블이름 (
    컬럼이름 타입 제약조건 키지정 ... ,
    컬럼이름 타입 조건,
    컬럼이름 타입 조건,
    키 제약 조건
);

alter table 테이블이름 add, modify, delete column 컬럼이름 조건등; */

-- board 테이블의 게시글 번호(bidx)를 참조하는 attach 테이블
-- aIDX : 정수, 자동부여, 기본키
-- oriName : 원본 파일 이름 문자열, NN, 중복가능, 260자
-- stoName : 저장 파일 이름 문자열, NN, 중복불가, 260자(uuid 36자)
-- bIDX : 정수, 참조키(board.bIDX)
-- ext : 확장자명, 문자열 
-- aType : 파일 종류 : / 압축, 이미지, 텍스트, 실행파일, 문서 등등

-- sql문 작성
create table attach (
    aIDX int unsigned auto_increment primary key comment '첨부 파일 번호',
    oriName varchar(260) NOT NULL comment '원본 파일 이름',
    stoName varchar(260) NOT NULL UNIQUE comment '저장 파일 이름',
    bIDX int NOT NULL comment '게시글 번호',
    ext varchar(10) NOT NULL comment '확장자',
    aType varchar(10) comment '파일 종류',
    FOREIGN KEY (bIDX) REFERENCES board (bIDX)
);
