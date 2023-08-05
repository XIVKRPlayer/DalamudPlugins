## Korea Dalamud Third-Party Plugins Repository
------------
### Dalamud 란 무엇인가요.
> 1. [Github:Goatcorp](https://goatcorp.github.io/) 에서 제작된 Dalamud는 XIVLauncher에 포함 되어있습니다.
> 2. 그러나 DalamudKR 디스코드 서버장을 시작으로 여러 인원을 거쳐 한국버전의 Dalamud 가 탄생되었습니다.
> 3. Dalamud는 완전한 외부 프로그램으로 FFXIV 는 이를 금기시 하고 있으며 실제로 사용을 들키거나 발각될 경우 계정이 정지됩니다.
> 4. FFXIV 서버 내에서 Dalamud 를 사용하지 안하는지 판단할 수 없으며 또한, FFXIV 서버에 영향을 주지 않습니다.

### XIVKRPlayer의 레포지토리
> 1. 이 레포지토리는 순수하게 추가하고 싶은 플러그인을 추가 및 배포하는 공간입니다. 그 어떤 수정도 하지 않았으며 플러그인은 순수하게 원본일 뿐입니다.
> 2. 해당 레포지토리는 게임내의 생활, 커스터마이즈, VFX 등 가벼운 플러그인만을 다루며 ESP, Rader 등 게임내 몬스터, 플레이어의 위치, 기술, 패턴을 추적하고 파악하는 플러그인은 추가하지 않습니다.\n
> 3. JsonGenerator?
>> JsonGenerator는 하드코딩된 Python 언어를 기반으로 한 프로그램입니다. 실행시 플러그인의 정보를 토대로 Repo.json 에 들어가기 위해 플러그인 별 Json 파일을 생성하는 프로그램입니다.
>> 다만 해당 프로그램은 현재 많은 문제와 불편함을 가지고 있어 소프트코딩으로 수정할 예정입니다.
------------
### 예정된 작업
> JsonGenerator.py
>> 확인된 문제:
>> 1. 5개 이상 플러그인 작성시 프로그램 종료됨.
>> 해결할 문제:
>> 1. 플러그인별로 Json이 생성되지 않고 기존 TestRepo.json 파일에 Append 되는 방식으로 수정해볼 예정.
