export default function getStudentIdsSum(stduList) {
    const sum = stduList.reduce((acc, current) => acc + current.id, 0);
    return sum;
}
