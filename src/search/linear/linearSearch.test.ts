import { NO_MATCH } from "../common";
import linearSearch from "./linearSearch";

describe('Linear Search', () => {

    test('Simple Strings', () => {
        const myList = ['Hotel', 'Alpha', 'Kilo', 'Charlie', 'Echo',
            'Foxtrot', 'Delta', 'Juliet', 'Lima', 'Golf', 'Bravo']

        // Normal data which is in the list
        const charlie = linearSearch(myList, 'Charlie')
        expect(charlie).toBe(3)

        // Edge cases
        const alpha = linearSearch(myList, 'Alpha')
        expect(alpha).toBe(1)

        const lima = linearSearch(myList, 'Lima')
        expect(lima).toBe(8)

        // Not found
        const bob = linearSearch(myList, 'bob')
        expect(bob).toBe(NO_MATCH)
    })

    test('Simple Numbers', () => {
        const items = [15, 7, 1, 8, 43, 9, 81, 5];
        const found = linearSearch(items, 8);

        expect(found).toBe(3);
    });
})