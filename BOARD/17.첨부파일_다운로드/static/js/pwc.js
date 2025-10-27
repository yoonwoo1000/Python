window.onload = function (){
    document.forms.pwform.addEventListener('submit',function(event){
        event.preventDefault() // 기본 작업 취소
        uPW = document.querySelector('[name=uPW]')  // 현재비번 입력 객체
        if ( uPW.value.trim() == '' ) {     // 현재비번 입력없음
            alert('현재 비번을 입력하세요')
            uPW.value = ''                  // 입력 내용을 지우고
            uPW.focus()                     // 입력칸으로 커서 이동
            return  // 함수 종료
        }
        // name="newPW" 의 value와 id="newPWC" 의 value가 같으면
        newPW = document.querySelector('[name=newPW]')
        if (newPW.value.trim() == '') {
            alert('새로운 비번을 입력하세요')
            newPW.value = ''
            newPW.focus()
            return
        }
        if (newPWC.value.trim() == '' ) {
            alert('비번확인을 입력하세요')
            newPWC.value = ''
            newPWC.focus()
            return
        }
        if (newPW.value == newPWC.value) {
            // form submit를 명시적으로 진행
            event.target.submit()
        }else{
            alert('비번확인이 잘못되었습니다')
            newPWC.value = ''
            newPWC.focus()
            return
        }
    })
}