## x만큼 간격이 있는 n개의 숫자

### **문제 설명**

> 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
> 

### **제한 조건**

- x는 -10000000 이상, 10000000 이하인 정수입니다.
- n은 1000 이하인 자연수입니다.

***코드***

```jsx
function solution(x, n) {
    var answer = [];
    return answer;
}
```

***풀이***

> 첫 예제 코드는 a,b에 각각 5와 3이 구해져 있었다.
> 

<aside>
💡 저걸 어떻게 담기만 하면 될텐데....

</aside>

> 아무리 생각해도 추상화가 머리속에 박혀있지 않은 나는 for문 중첩으로 돌리는 방법밖에 몰랐고, 그렇게 푼뒤 다른 사람분들 풀이를 보니 repeat()함수가 있는걸 알게 되었다.
> 

***내 풀이***

```jsx
function solution(x, n) {
    let answer = [];
    let y = x;

    for(let i = 0; i < n; i++){
        answer[i] = x;
        x = y + x;
    }
    return answer;
}
```

***다른 풀이***

```jsx
function solution(x, n) {
    return Array(n).fill(x).map((v, i) => (i + 1) * v)
}
```

> 갭차이 많이 느낀다.
