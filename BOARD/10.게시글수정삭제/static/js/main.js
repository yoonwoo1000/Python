window.onload = function (){
    typeSelect.addEventListener('change',function(event){
        //alert(event.target)
        console.log(event.target.value)
        // 페이지를 이동시킴
        window.location.href = `/?type=${event.target.value}`
    })
}