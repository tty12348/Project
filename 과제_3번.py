import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password_hash = self._hash_password(password)

    def display(self):
        print(f"이름: {self.name}, 아이디: {self.username}")

    def _hash_password(self, password):
        # hashhlib을 사용하여 비밀번호 해싱
        sha256 = hashlib.sha256()
        sha256.update(password.encode('uft-80'))
        return sha256.hexdigest()

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

# members, posts 리스트 초기화
members = []
posts = []

# 회원 인스턴스 생성
name = input("이름을 입력하세요: ")
username = input("아이디를 입력하세요: ")
password =  input("비밀번호를 입력하세요: ")
member1 = Member(name, username, password)

# members 리스트에 회원 인스턴스 추가
members.append(member1)

# 회원 이름 출력
print("\n회원 이름들:")
for member in members:
    member.display()

# 게시글 인스턴스 생성
title = input("\n게시글 제목을 입력하세요:")
content = input("게시글 내용을 입력하세요: ")
author = input("작성자 아이디를 입력하세요: ")
post1 = Post(title, content, author)

# posts 리스트에 게시글 인스턴스 추가
posts.append(post1)

# 특정 유저가 작성한 게시글 제목 출력
print(f"\n{author}가 작성한 게시글 제목:")
for post in posts:
    if post.author == author:
        print(post.title)