import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clojure running')
@cli.command()
def start(): click.echo('clojure started')
if __name__ == '__main__': cli()
