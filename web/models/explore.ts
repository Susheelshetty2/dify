import type { AppMode } from './app'

export type AppBasicInfo = {
  id: string
  name: string
  mode: AppMode
  icon: string
  icon_background: string
  is_agent: boolean
}

export type AppCategory = 'Writing' | 'Translate' | 'HR' | 'Programming' | 'Assistant'

export type App = {
  app: AppBasicInfo
  app_id: string
  description: string
  copyright: string
  privacy_policy: string
  category: AppCategory
  position: number
  is_listed: boolean
  install_count: number
  installed: boolean
  editable: boolean
  is_agent: boolean
}

export type InstalledApp = {
  app: AppBasicInfo
  id: string
  uninstallable: boolean
  is_pinned: boolean
}
