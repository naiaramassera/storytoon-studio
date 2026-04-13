'use client'

import { useState } from 'react'
import { Header } from '../../../components/Header'
import { apiPost } from '../../../lib/api'

export default function NewEpisodePage() {
  const [seriesId, setSeriesId] = useState('1')
  const [title, setTitle] = useState('')
  const [storyText, setStoryText] = useState('')
  const [duration, setDuration] = useState('10')
  const [episodeId, setEpisodeId] = useState<number | null>(null)
  const [outline, setOutline] = useState<string>('')
  const [message, setMessage] = useState('')

  async function handleCreate(e: React.FormEvent) {
    e.preventDefault()
    const data = await apiPost('/episodes', {
      series_id: Number(seriesId),
      title,
      story_text: storyText,
      target_duration_minutes: Number(duration),
    })
    const id = (data as { id: number }).id
    setEpisodeId(id)
    setMessage(`Episódio criado. ID: ${id}`)
  }

  async function handleOutline() {
    if (!episodeId) return
    const data = await apiPost(`/episodes/${episodeId}/build-outline`, {})
    setOutline(JSON.stringify((data as { outline: unknown }).outline, null, 2))
  }

  async function handleRender() {
    if (!episodeId) return
    await apiPost(`/episodes/${episodeId}/render`, {})
    setMessage((prev) => `${prev} | Renderização enviada para fila.`)
  }

  return (
    <div>
      <Header />
      <div className="grid gap-6 lg:grid-cols-2">
        <form onSubmit={handleCreate} className="card space-y-4">
          <h2 className="text-2xl font-semibold">Novo episódio</h2>
          <input className="input" placeholder="ID da série" value={seriesId} onChange={(e) => setSeriesId(e.target.value)} />
          <input className="input" placeholder="Título do episódio" value={title} onChange={(e) => setTitle(e.target.value)} />
          <input className="input" placeholder="Duração em minutos" value={duration} onChange={(e) => setDuration(e.target.value)} />
          <textarea className="input min-h-64" placeholder="Cole aqui a história completa" value={storyText} onChange={(e) => setStoryText(e.target.value)} />
          <div className="flex flex-wrap gap-3">
            <button className="btn" type="submit">Criar episódio</button>
            <button className="rounded-xl border border-slate-700 px-4 py-3" type="button" onClick={handleOutline}>Gerar outline</button>
            <button className="rounded-xl border border-slate-700 px-4 py-3" type="button" onClick={handleRender}>Renderizar</button>
          </div>
          {message ? <p className="text-emerald-400">{message}</p> : null}
        </form>
        <div className="card">
          <h3 className="mb-3 text-xl font-semibold">Outline gerado</h3>
          <pre className="max-h-[70vh] overflow-auto whitespace-pre-wrap text-sm text-slate-300">{outline || 'Ainda não gerado.'}</pre>
        </div>
      </div>
    </div>
  )
}
