import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('leiningen running')
@cli.command()
def start(): click.echo('leiningen started')
if __name__ == '__main__': cli()
