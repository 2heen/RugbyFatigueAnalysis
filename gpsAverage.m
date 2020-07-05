file = csvread('gps2.csv');
numLines = size(file)
totalX = zeros(1, 21);
totalY = zeros(1, 21);
totalZ = zeros(1, 21);
count = zeros(1, 21);
for x = 1:1:size(file(:, 1))
    totalX(file(x, 1)) = totalX(file(x, 1)) + file(x, 2);
    totalY(file(x, 1)) = totalY(file(x, 1)) + file(x, 3);
    totalZ(file(x, 1)) = totalZ(file(x, 1)) + file(x, 4);
    count(file(x, 1)) = count(file(x, 1)) + 1;
end
averageX = zeros(1, 21);
averageY = zeros(1, 21);
averageZ = zeros(1, 21);
for x = 1:1:size(averageX, 2)
    averageX(x) = totalX(x) / count(x);
    averageY(x) = totalY(x) / count(x);
    averageZ(x) = totalZ(x) / count(x);
end
magnitude = zeros(1, 21);
for x = 1:1:size(magnitude, 2)
    magnitude(x) = power((power(averageX(x), 2) + power(averageY(x), 2) + power(averageZ(x), 2)), 0.5);
end

magnitude2 = zeros(1, 21);
for x = 1:1:size(file(:, 1))
    magnitude2(file(x, 1)) = magnitude2(file(x, 1)) + power((power(file(x, 2), 2) + power(file(x, 3), 2) + power(file(x, 4), 2)), 0.5);
end
for x = 1:1:size(magnitude2, 2)
    magnitude2(x) = magnitude2(x) / count(x);
end