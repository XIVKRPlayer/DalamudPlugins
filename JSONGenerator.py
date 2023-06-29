import json
import clipboard
from collections import OrderedDict

#기초변수
null = None
Tags = []
ImageUrls = []
DefaultDir = "https://raw.githubusercontent.com/XIVKRPlayer/DalamudPlugins/master/Plugins/"

#설정값 지정
Author = input("Author : ")
Name = input("Name : ")
Punchline = input("Punchline : ")
Description = input("Description : ")
#Tags
ExistQ_tagurl = input("태그가 있습니까?(y/n 기본:y) : ")
if ExistQ_tagurl == "y" or ExistQ_tagurl == "Y" or ExistQ_tagurl == "":
    print("Tag를 입력해주세요. 'done' 입력시 종료됩니다.")
    while True:
        Insert = input("Tag is... ")
        if Insert == "done":
            break
        else:
            Tags.append(Insert)
else:
    print("Tag 입력이 종료되었습니다.")
print("자동입력: "+Name+" [엔터]")
InternalName = input("InternalName : ")
if InternalName == "":
    InternalName = Name
AssemblyVersion = input("AssemblyVersion : ")
AutoRepo = "https://github.com/"+Author+"/"+InternalName
print("자동입력: "+AutoRepo+" [엔터]")
RepoUrl = input("RepoUrl : ")
if RepoUrl == "":
    RepoUrl = AutoRepo
print("기본값 : 8")
DalamudApiLevel = input("DalamudApiLevel : ")
if DalamudApiLevel == "":
    DalamudApiLevel = 8
DownloadLink = DefaultDir+InternalName+"/latest.zip"
#ImageUrls
print("이미지 갯수를 입력해주세요.(기본값:0)")
Count = input("입력 : ")
if Count == "0" or Count == "":
    ImageUrls = null
else:
    for i in range(int(Count)):
        ii = str(i+1)
        ImageUrls.append(DefaultDir+InternalName+"/images/"+"image"+ii+".png")
#IconUrl
print("아이콘이 있습니까?(기본값:y)")
IconYN = input("입력: ")
if IconYN == "y" or IconYN == "Y" or IconYN == "":
    IconUrl = (DefaultDir+InternalName+"/images/"+"icon.png")
else:
    IconUrl = null

#JSON 세팅
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
    "RepoUrl": RepoUrl,
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

#Json출력
FileName = "OutPut/"+InternalName+".json"
with open(FileName, 'w') as outfile:
    json.dump(file_data, outfile, indent=4)
