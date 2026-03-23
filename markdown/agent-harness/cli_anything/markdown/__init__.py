import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('markdown running')
@cli.command()
def start(): click.echo('markdown started')
if __name__ == '__main__': cli()
