import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jenkinsfile running')
@cli.command()
def start(): click.echo('jenkinsfile started')
if __name__ == '__main__': cli()
