import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Traefik running on :8080')
@cli.command()
def routes(): click.echo('Frontend/Backend routes')
@cli.command()
def services(): click.echo('Managed services')
if __name__ == '__main__': cli()
