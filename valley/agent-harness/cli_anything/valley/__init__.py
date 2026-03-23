import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('valley running')
@cli.command()
def start(): click.echo('valley started')
if __name__ == '__main__': cli()
