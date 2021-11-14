import { NO_MATCH } from "../common";
import binarySearch from "./binarySearch";

describe('Binary Search', () => {

    test('Simple Strings', () => {
        const myList = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo',
            'Foxtrot', 'Golf', 'Hotel', 'Juliet', 'Kilo', 'Lima']

        // Normal data which is in the list
        const charlie = binarySearch(myList, 'Charlie')
        expect(charlie).toBe(2)

        // Edge cases
        const alpha = binarySearch(myList, 'Alpha')
        expect(alpha).toBe(0)

        const lima = binarySearch(myList, 'Lima')
        expect(lima).toBe(10)

        // Not found
        const bob = binarySearch(myList, 'bob')
        expect(bob).toBe(NO_MATCH)
    })

    test('Simple Numbers', () => {
        const items = [1, 2, 3, 4, 5, 7, 10, 43];
        const found = binarySearch(items, 7);

        expect(found).toBe(5);
    });
})