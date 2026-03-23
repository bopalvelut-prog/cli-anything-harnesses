import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('swing running')
@cli.command()
def start(): click.echo('swing started')
if __name__ == '__main__': cli()
