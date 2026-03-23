import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asm running')
@cli.command()
def start(): click.echo('asm started')
if __name__ == '__main__': cli()
