# 총 게시글 수와, 페이지당 게시글 수로 최대 페이지 번호 계산하기
total = 21                      # 총 게시글 개수
perPage = 10                    # 페이지당 게시글 수
MaxPage = total//perPage + 1    # 마지막 페이지번호
print(MaxPage)
# 위의 계산식은 10개, 20개, 30개 일때에 오류
# 1~10 : 1 / 11~20 : 2 / 21~30 : 3
total = 10                      # 게시글이 10개일때
MaxPage = total//perPage + 1
if total % perPage == 0 :       # perPage의 배수일때
    MaxPage -= 1                # 1을 빼줌
print(MaxPage)
# 한번에 계산하기
MaxPage = ( total - 1 ) // perPage + 1
print(MaxPage)

print('게시글 번호와, 페이지 번호 확인하기 ------ ')
nums = (1,9,10,11,19,20,21,29,30,31,39,40,41)
for num in nums :
    print("게시글번호 : ", num)
    pageNum = num // perPage + 1
    if num % perPage == 0 :
        pageNum -= 1
    print( f'{num}번 게시글은 {pageNum}번 페이지에 있습니다')
    pageNum = (num-1) // perPage + 1
    print( f'{num}번 게시글은 {pageNum}번 페이지에 있습니다')
