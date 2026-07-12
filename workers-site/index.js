import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

addEventListener('fetch', event => {
  event.respondWith(handleEvent(event));
});

async function handleEvent(event) {
  return getAssetFromKV(event, {
    mapRequestToAsset: request => {
      const url = new URL(request.url);
      if (url.pathname.endsWith('/')) {
        return new Request(`${url.origin}${url.pathname}index.html`, request);
      }
      return request;
    }
  });
}
