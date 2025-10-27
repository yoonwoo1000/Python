window.onload = function(){
    function toggleTr(rIDX) { // 댓글 번호로 tr 토글하는 함수
        obj = document.querySelector(`tr[data-reply-id='${rIDX}']`)
        if( obj.style.display == 'none') { 
            obj.style.display = 'table-row'
        }else{ obj.style.display = 'none' }
    }
    modify_BTNS = document.querySelectorAll('.modify_BTN') // 모든 수정버튼
    modify_BTNS.forEach(element => { // 각각의 수정하기 버튼에
        element.addEventListener('click', function(event){ // 클릭 이벤트
            console.log(event.currentTarget) // 이벤트 발생 객체
            toggleTr(event.currentTarget.dataset.replyId) // 댓글번호로 토글
        })
    });
    cancel_BTNS = document.querySelectorAll('.cancel_BTN') // 모든 취소버튼
    cancel_BTNS.forEach(element => {
        element.addEventListener('click', function(event){
            toggleTr(event.currentTarget.dataset.replyId)
        })
    });
}