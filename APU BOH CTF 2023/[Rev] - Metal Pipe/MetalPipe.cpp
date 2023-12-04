#include <Windows.h>
#include <iostream>
#include <thread>

using namespace std;

const int MESSAGE_SIZE = 512;
const string flag = "ABOH{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}";

int Server()
{
	LPCWSTR pwsPipeName = L"\\\\.\\pipe\\battle-of-hackers";
	HANDLE hServerPipe;
	HANDLE hFile = NULL;
	BOOL bSuccess;
	BOOL bPipeRead = TRUE;
	LPWSTR pReadBuf[MESSAGE_SIZE] = { 0 };
	LPDWORD pdwBytesRead = { 0 };

	hServerPipe = CreateNamedPipe(
		pwsPipeName,
		PIPE_ACCESS_INBOUND,
		PIPE_TYPE_MESSAGE | PIPE_NOWAIT,
		PIPE_UNLIMITED_INSTANCES,
		2048,
		2048,							
		20000,
		NULL
	);

	bSuccess = ConnectNamedPipe(hServerPipe, NULL);
	wprintf(L"Connected\n");
	Sleep(300);

	bPipeRead = ReadFile(hServerPipe, pReadBuf, MESSAGE_SIZE, pdwBytesRead, NULL);
	CloseHandle(hServerPipe);

	return 0;
}

int main()
{	
	for (int i = 45; i >= 0; i--) {
		std::thread t1(Server);
		Sleep(300);

		LPCWSTR pwsPipeName = L"\\\\.\\pipe\\battle-of-hackers";
		HANDLE hFile = NULL;
		DWORD dwFlags = 0;
		BOOL bSuccess;
		DWORD bytesWritten = 0;
		DWORD messageLength;

		hFile = CreateFile(pwsPipeName, GENERIC_WRITE, 0, NULL, OPEN_EXISTING, dwFlags, NULL);
		bSuccess = WriteFile(hFile, &flag[i], 1, &bytesWritten, NULL);
		CloseHandle(hFile);

		t1.join();
		PlaySound(MAKEINTRESOURCE(IDR_WAVE1), NULL, SND_RESOURCE);
	}

	return 0;
}