var board = [
  {
    id: 2,
    title: "제목1",
    content: "내용1",
    createdate: new Date(),
  },
  {
    id: 3,
    title: "제목1",
    content: "내용1",
    createdate: new Date(),
  },
  {
    id: 4,
    title: "제목1",
    content: "내용1",
    createdate: new Date(),
  },
  {
    id: 5,
    title: "제목1",
    content: "내용1",
    createdate: new Date(),
  },
]

db.board.save(board);
db.board.find().pretty();

