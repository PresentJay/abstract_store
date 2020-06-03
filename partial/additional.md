# additional Knowledges

# from @Jay Present

> Git log 예쁘게 보기

[[Git] log 예쁘게 보기](https://developer-alle.tistory.com/320?category=826739)

터미널에 아래 명령어 입력 후 "git lg" 실행

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

> git rm 명령어 (로컬/원격 파일 삭제 명령어)

[[Git] Github에 잘못 올라간 파일 삭제하기 - Heee's Development Blog](https://gmlwjd9405.github.io/2018/05/17/git-delete-incorrect-files.html)

git rm —cached [filename]   // 이게 로컬에서는 삭제 안 하고 원격에서만 삭제하는 거!

> git rebase vs git merge 차이점?

[Git merge, rebase 이해하기](https://cyberx.tistory.com/96)

merge commit이 남지 않아요

> git branch 생성 / 삭제

git checkout -b [branch_name]    // 생성

git branch -d [branch_name]     // 삭제