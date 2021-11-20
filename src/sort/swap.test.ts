import swap from "./swap";

describe('Swap', () => {
    test('Simple', () => {
        const myList = [1, 2, 3, 4, 5, 6, 7, 8];
        swap(myList, 1, 2);
        expect(myList[1]).toBe(3);
        expect(myList[2]).toBe(2);
    })
})