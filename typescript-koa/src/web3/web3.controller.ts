import * as Koa from 'koa';
import * as Router from 'koa-router';
import { getRepository, Repository } from 'typeorm';
import * as HttpStatus from 'http-status-codes';

const routerOpts: Router.IRouterOptions = {
  prefix: '/web3',
};

const router: Router = new Router(routerOpts);

router.get('/', async (ctx:Koa.Context) => {
});

router.post('/', async (ctx:Koa.Context) => {
  // 通过POST，接受签名信息，进而确认地址的真正拥有者
  ctx.body = {
    data: {},
  };
});

export default router;
