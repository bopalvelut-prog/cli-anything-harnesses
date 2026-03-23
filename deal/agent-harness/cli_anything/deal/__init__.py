import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deal running')
@cli.command()
def start(): click.echo('deal started')
if __name__ == '__main__': cli()
