const swap = (arr: any[], i: number, j: number) => {
    const s = arr[i];
    arr[i] = arr[j];
    arr[j] = s;
}

export default swap;