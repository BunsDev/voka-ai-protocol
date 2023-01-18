import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export default class NFT {

  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  name: string;

  @Column()
  description: string;

  @Column()
  properties: string;

  @Column()
  minted: Number;

  @Column()
  contract_address: string;

  @Column()
  token_id: string;

  @Column()
  token_standard: string;

  @Column()
  chain: string;

  @Column({nullable: true})
  ipfs_uri: string;

  @Column({nullable: true})
  mint_time: string;

  @Column()
  owner_address: string;
}
