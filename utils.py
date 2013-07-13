def unpack(first, *rest):
    return first, rest

def include(prefix, module_path):
    module = __import__(module_path, globals(), locals(), fromlist=["*"])
    urls = getattr(module, 'urls')
    final_urls = list()
    for url in urls:
        pattern, rest = unpack(*url)
        if pattern.startswith("/"):
            pattern = r"%s%s" % (prefix, pattern[1:])
        else:
            pattern = r"%s%s" % (prefix, pattern)
        final_urls.append((pattern,) + rest)
    return final_urls