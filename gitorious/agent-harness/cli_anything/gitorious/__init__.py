import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gitorious running')
@cli.command()
def start(): click.echo('gitorious started')
if __name__ == '__main__': cli()
