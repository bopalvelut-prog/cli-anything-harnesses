import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('roadmap running')
@cli.command()
def start(): click.echo('roadmap started')
if __name__ == '__main__': cli()
