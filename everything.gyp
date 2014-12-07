# Build EVERYTHING.
# xuxiang@mail.bnu.edu.cn
{
  'targets': [
    {
      'target_name': 'everything',
      'type': 'none',
      'dependencies': [
        'gyp/mapping.gyp:mapping',
        'gyp/cache.gyp:cache',
      ],
    },
  ],
}
