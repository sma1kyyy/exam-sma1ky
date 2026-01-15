FROM golang:1.24-alpine3.22 AS builder

WORKDIR /app

COPY go.mod ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o api-service ./cmd/api-service/main.go

FROM alpine:3.22

RUN apk --no-cache add ca-certificates

WORKDIR /app

COPY --from=builder /app/api-service .

CMD ["./api-service"]