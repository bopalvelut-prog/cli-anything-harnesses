import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grab running')
@cli.command()
def start(): click.echo('grab started')
if __name__ == '__main__': cli()
