import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('github_enterprise running')
@cli.command()
def start(): click.echo('github_enterprise started')
if __name__ == '__main__': cli()
