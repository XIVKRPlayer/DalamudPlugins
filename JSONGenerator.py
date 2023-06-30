import json
from collections import OrderedDict
import os

#기초변수
Working = True
DirPath = "Output/"
null = None
AddedPlugins = []
Tags = []
ImageUrls = []
DefaultDir = "https://raw.githubusercontent.com/XIVKRPlayer/DalamudPlugins/master/Plugins/"

#기초파일
file_data = {
    
}

#폴더생성 및 초기파일 생성
if not os.path.exists(DirPath): #폴더가 없으면 생성
    os.makedirs(DirPath)


#-----[함수섹터]-----
#설정값 지정
def main():
    global Author, Name, Punchline, Description, Tags, InternalName, AddedPlugins, AssemblyVersion, RepoUrl, DalamudApiLevel, DownloadLink, ImageUrls, IconUrl
    Author = input("Author : ")
    Name = input("Name : ")
    Punchline = input("Punchline : ")
    Description = input("Description : ")
    #Tags
    print("태그가 있습니까?(기본값:y)")
    print("yes or y = 확인, no or n = 취소, 기본값 = yes")
    ExistQ_tagurl = input("입력 : ")
    if ExistQ_tagurl.lower() in ["yes", "y", ""]:
        print("Tag를 입력해주세요. 'done' 입력시 종료됩니다.")
        while True:
            Insert = input("Tag is... ")
            if Insert.lower() in ["done"]:
                Insert = null
                break
            else:
                Tags.append(Insert)
    else:
        print("Tag 입력이 종료되었습니다.")
    print("InternalName 자동입력됨: "+Name)
    InternalName = input("InternalName : ")
    if InternalName == "":
        InternalName = Name
    AddedPlugins.append(InternalName) #현재까지 추가된 플러그인 목록
    AssemblyVersion = input("AssemblyVersion : ")
    RepoUrl = input("RepoUrl : https://github.com/")
    print("DalamudApiLevel 기본값 = 8")
    DalamudApiLevel = input("DalamudApiLevel : ")
    if DalamudApiLevel == "":
        DalamudApiLevel = 8
    DownloadLink = DefaultDir+InternalName+"/latest.zip"
    #ImageUrls
    print("이미지 갯수를 입력해주세요.(기본값:0)")
    Count = input("입력 : ")
    if Count.lower() in ["0" , ""]:
        ImageUrls = null
    else:
        for i in range(int(Count)):
            ii = str(i+1)
            ImageUrls.append(DefaultDir+InternalName+"/images/"+"image"+ii+".png")
    #IconUrl
    print("아이콘이 있습니까?(기본값:y)")
    print("yes or y = 확인, no or n = 취소, 기본값 = yes")
    IconYN = input("입력: ")
    if IconYN.lower() in ["yes", "y", ""]:
        IconUrl = (DefaultDir+InternalName+"/images/"+"icon.png")
    else:
        IconUrl = null
#JSON 세팅
def JSONSet():
    global file_data
    file_data = {
        "Author": Author,
        "Name": Name,
        "Punchline": Punchline,
        "Description": Description,
        "Changelog": "-",
        "Tags": Tags,
        "CategoryTags": null,
        "IsHide": False,
        "InternalName": InternalName,
        "AssemblyVersion": AssemblyVersion,
        "TestingAssemblyVersion": null,
        "IsTestingExclusive": False,
        "RepoUrl": "https://github.com/"+RepoUrl,
        "ApplicableVersion": "any",
        "DalamudApiLevel": DalamudApiLevel,
        "DownloadCount": 0,
        "LastUpdate": 0,
        "DownloadLinkInstall": DownloadLink,
        "DownloadLinkUpdate": DownloadLink,
        "DownloadLinkTesting": DownloadLink,
        "LoadPriority": 0,
        "ImageUrls": ImageUrls,
        "IconUrl": IconUrl,
        "AcceptsFeedback": True,
        "FeedbackMessage":null,
        "FeedbackWebhook":null,
        "_isDip17Plugin":True,
        "_Dip17Channel":"stable"
    }

#-----[작업섹터]-----
while Working == True:
    main() #변수 입력
    JSONSet() #JSON 값 출력
    with open(DirPath+InternalName+".json", 'w') as outfile: #JSON 만들기
        json.dump(file_data, outfile, indent=4)
    print("[ 현재 추가된 목록 ]")
    for x in range (int(len(AddedPlugins))): #작성한 플러그인만큼 출력.
        print(" - "+AddedPlugins[x])
    print("내용을 추가하시겠습니까?")
    print("yes or y = 확인, no or n = 취소, 기본값 = yes")
    ResetPoint = input(" >> ")
    if ResetPoint.lower() in ["y", "yes", ""]:
        Working = True
    elif ResetPoint.lower() in ["n", "no"]:
        Working = False
else:
    print("JSON 입력이 종료되었습니다.")