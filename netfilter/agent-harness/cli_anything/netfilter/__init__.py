import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('netfilter running')
@cli.command()
def start(): click.echo('netfilter started')
if __name__ == '__main__': cli()
