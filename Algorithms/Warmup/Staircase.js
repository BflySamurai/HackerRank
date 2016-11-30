//https://www.hackerrank.com/challenges/staircase

function main() {
    var n = parseInt(readLine());
    for (i=1; i<n+1; i++) {
        line = Array(1+n-i).join(" ") + Array(1+i).join("#")
        console.log(line)
    }
}
