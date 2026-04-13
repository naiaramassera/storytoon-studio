import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'StoryToon Studio',
  description: 'Crie séries animadas com personagens consistentes.',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>
        <main className="mx-auto min-h-screen max-w-6xl px-6 py-8">{children}</main>
      </body>
    </html>
  )
}
