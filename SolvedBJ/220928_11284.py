'''
초성 (19): ㄱ, ㄲ, ㄴ, ㄷ, ㄸ, ㄹ, ㅁ, ㅂ, ㅃ, ㅅ, ㅆ, ㅇ, ㅈ, ㅉ, ㅊ, ㅋ, ㅌ, ㅍ, ㅎ
중성 (21): ㅏ, ㅐ, ㅑ, ㅒ, ㅓ, ㅔ, ㅕ, ㅖ, ㅗ, ㅘ, ㅙ, ㅚ, ㅛ, ㅜ, ㅝ, ㅞ, ㅟ, ㅠ, ㅡ, ㅢ, ㅣ
종성 (28): _, ㄱ, ㄲ, ㄱㅅ, ㄴ, ㄴㅈ, ㄴㅎ, ㄷ, ㄹ, ㄹㄱ, ㄹㅁ, ㄹㅂ, ㄹㅅ, ㄹㅌ, ㄹㅍ,
    ㄹㅎ, ㅁ, ㅂ, ㅂㅅ, ㅅ, ㅆ, ㅇ, ㅈ, ㅊ, ㅋ, ㅌ, ㅍ, ㅎ
44032를 뺀 수를
21 * 28로 나눔 -> 몫 = 초성
나머지를 28로 나눔 -> 몫 = 중성
나머지 = 종성
'''

chosung = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
jungsung = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
jongsung = ' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'

utf = ord(input().rstrip()) - ord('가')
cho = utf // len(jungsung) // len(jongsung)
jung = utf // len(jongsung) % len(jungsung)
jong = utf % len(jongsung)

print(chosung[cho], jungsung[jung], jongsung[jong], sep='\n')
