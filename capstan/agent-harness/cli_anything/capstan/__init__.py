import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('capstan running')
@cli.command()
def start(): click.echo('capstan started')
if __name__ == '__main__': cli()
