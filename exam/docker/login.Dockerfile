FROM golang:1.24-alpine3.22 AS builder

WORKDIR /app

COPY go.mod ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o login-service ./cmd/login-service/main.go

FROM alpine:3.22

WORKDIR /app

COPY --from=builder /app/login-service .

CMD ["./login-service"]