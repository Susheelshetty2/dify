import type { FC } from 'react'
import type { ChatItem } from '../../types'
import { Markdown } from '@/app/components/base/markdown'

type BasicContentProps = {
  item: ChatItem
}
const BasicContent: FC<BasicContentProps> = ({
  item,
}) => {
  const {
    annotation,
    content,
  } = item

  if (annotation?.logAnnotation)
    return <Markdown content={annotation?.logAnnotation.content || ''} />

  return <Markdown content={content} />
}

export default BasicContent
