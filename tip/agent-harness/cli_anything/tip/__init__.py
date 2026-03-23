import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tip running')
@cli.command()
def start(): click.echo('tip started')
if __name__ == '__main__': cli()
