import { SortAlgorithm } from "./common";

const sortTest = (sort: SortAlgorithm<any>) => () => {
    test('Strings', () => {
        const names: string[] = [
            "Lister",
            "Cat",
            "Kryten",
            "Rimmer",
            "Holly",
            "Kochanski",
        ];

        const sortedNames: string[] = sort(names);

        expect(sortedNames).toStrictEqual([
            "Cat",
            "Holly",
            "Kochanski",
            "Kryten",
            "Lister",
            "Rimmer",
        ]);
    });

    test('Numbers', () => {
        const numbers: number[] = [5, 7, 12, 3, 2, 9, 1, 4, 0, 8];

        const sortedNumbers: number[] = sort(numbers);

        expect(sortedNumbers).toStrictEqual([0, 1, 2, 3, 4, 5, 7, 8, 9, 12])
    })
}

export default sortTest;