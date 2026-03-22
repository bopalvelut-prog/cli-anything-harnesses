import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def balance(): subprocess.run(['solana', 'balance'])
@cli.command()
def transfer(): click.echo('Solana transfer')
if __name__ == '__main__': cli()
