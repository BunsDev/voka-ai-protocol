import * as Koa from 'koa';
import * as Router from 'koa-router';
import { getRepository, Repository } from 'typeorm';
import nftEntity from './nft.entity';
import * as HttpStatus from 'http-status-codes';

const routerOpts: Router.IRouterOptions = {
  prefix: '/nft',
};

const router: Router = new Router(routerOpts);

router.get('/', async (ctx:Koa.Context) => {
  // Get the nft repository from TypeORM.
  const nftRepo:Repository<nftEntity> = getRepository(nftEntity);

  // Find the requested nft.
  const nfts = await nftRepo.find();

  // Respond with our nft data.
  ctx.body = {
    data: { nfts },
  };
});

router.get('/:nft_id', async (ctx:Koa.Context) => {
  // Get the movie repository from TypeORM.
  const nftRepo:Repository<nftEntity> = getRepository(nftEntity);

  // Find the requested nft.
  const nft = await nftRepo.findOneBy({id:ctx.params.nft_id});

  // If the nft doesn't exist, then throw a 404.
  // This will be handled upstream by our custom error middleware.
  if (!nft) {
    ctx.throw(HttpStatus.NOT_FOUND);
  }

  // Respond with our nft data.
  ctx.body = {
    data: { nft },
  };
});

router.post('/', async (ctx:Koa.Context) => {
  // Get the nft repository from TypeORM.
  const nftRepo:Repository<nftEntity> = getRepository(nftEntity);

  // Create our new nft.
  const nft: nftEntity = nftRepo.create(ctx.request.body);

  // Persist it to the database.
  await nftRepo.save(movie);

  // Set the status to 201.

  // Respond with our nft data.ctx.status = HttpStatus.CREATED;
  ctx.body = {
    data: { nft },
  };
});

export default router;
