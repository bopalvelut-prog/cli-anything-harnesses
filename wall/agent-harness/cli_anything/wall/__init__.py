import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wall running')
@cli.command()
def start(): click.echo('wall started')
if __name__ == '__main__': cli()
