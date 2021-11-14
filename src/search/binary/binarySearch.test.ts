import binarySearch from "./binarySearch";

describe('Binary Search', () => {

    test('Simple Numbers', () => {
        const items = [1, 2, 3, 4, 5, 7, 10, 43];
        const found = binarySearch(items, 7);

        expect(found).toBe(5);
    })
})