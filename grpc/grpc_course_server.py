from concurrent import futures

import grpc

from grpc import course_service_pb2, course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):

    def GetCourse(self, request, context):
        """Метод GetCourse обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetUser о курсе: {request.course_id}')

        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )


def serve():
    """Функция создает и запускает gRPC-сервер"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    server.add_insecure_port('[::]:50051')

    server.start()
    print("gRPC сервер запущен на порту 50051...")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()