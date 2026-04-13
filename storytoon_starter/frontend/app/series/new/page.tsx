'use client'

import { useState } from 'react'
import { Header } from '../../../components/Header'
import { apiPost } from '../../../lib/api'

export default function NewSeriesPage() {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [message, setMessage] = useState('')

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    const data = await apiPost('/series', {
      title,
      description,
      visual_style: 'cartoon 2D',
      audience: 'infantil',
      language: 'pt-BR',
    })
    setMessage(`Série criada com sucesso. ID: ${(data as { id: number }).id}`)
    setTitle('')
    setDescription('')
  }

  return (
    <div>
      <Header />
      <form onSubmit={handleSubmit} className="card mx-auto max-w-2xl space-y-4">
        <h2 className="text-2xl font-semibold">Criar nova série</h2>
        <input className="input" placeholder="Nome da série" value={title} onChange={(e) => setTitle(e.target.value)} />
        <textarea className="input min-h-32" placeholder="Descrição" value={description} onChange={(e) => setDescription(e.target.value)} />
        <button className="btn" type="submit">Salvar série</button>
        {message ? <p className="text-emerald-400">{message}</p> : null}
      </form>
    </div>
  )
}
